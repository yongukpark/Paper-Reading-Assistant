# String Concatenation(+=) vs List Accumulation + join()

챗봇을 구현하다보면 llm.stream()을 사용하여 llm의 출력을 받을 때가 있다.
이때 필요에 따라 스트리밍되는 문자를 이어 붙여 저장하는 경우도 종종있다.

대부분 아무런 의심없이 다음과 같이 코드를 짤 것이다.

```python
chunks = []
for chunk in chain.stream():
    print(chunk, end="", flush=True)
    chunks.append(chunk)
```

직관적이고 읽기도 쉽다.

그런데 chunk 개수가 많아지면 이 방식은 생각보다 비효율적이다.
그래서 실제로는 보통 이런 방식이 더 많이 쓰인다.

```python
chunks = []
for chunk in chain.stream():
    print(chunk, end="", flush=True)
    chunks.append(chunk)

response = "".join(parts)
```

이번 글에서는 이 둘이 왜 차이가 무엇인지, 아주 간단한 실험으로 정리해보려고 한다.

## 간단한 실험

실험 코드는 정말 단순하다.

```python
import time

for n in [100, 1000, 10000, 100000, 200000]:
    print(f"\n{'='*10} n={n} {'='*10}")
    
    chunks = ["hello"] * n

    # 1. += 방식
    start = time.perf_counter()
    response = ""
    for chunk in chunks:
        response += chunk
    end = time.perf_counter()
    plus_time = end - start

    # 2. append + join 방식
    start = time.perf_counter()
    parts = []
    for chunk in chunks:
        parts.append(chunk)
    response = "".join(parts)
    end = time.perf_counter()
    join_time = end - start

    speedup = plus_time / join_time if join_time > 0 else float("inf")

    print(f"{'+=':<20} : {plus_time:>10.8f} sec")
    print(f"{'append + join':<20} : {join_time:>10.8f} sec")
    print(f"{'speedup (+= / join)':<20} : {speedup:>10.2f}x")
```



![alt text](../img/append_join.png)



n이 클수록 `append() + join()` 쪽의 속도가 급격하게 빠르다는 것을 인지할 수 있다.

## 왜 차이가 날까?

이유는 Python 문자열의 특성 때문이다.

문자열은 **immutable**, 즉 불변 객체다.  
한 번 만들어진 문자열은 내부 내용을 직접 바꿀 수 없다.

그래서 이런 코드가 실행될 때:

```python
response += chunk
```

실제로는 기존 문자열 뒤에 붙이는 게 아니라,

1. 기존 문자열 내용을 복사하고
2. 새 chunk를 뒤에 붙여서
3. 새로운 문자열 객체를 다시 만든다

는 일이 반복된다.

즉, chunk가 많아질수록 매번 더 긴 문자열을 새로 복사하게 된다.

반면 리스트는 다르다.

```python
parts.append(chunk)
```

이건 문자열 전체를 매번 다시 만드는 게 아니라,  
리스트에 조각을 하나씩 쌓아두는 동작이다.

그리고 마지막에:

```python
"".join(parts)
```

로 한 번만 전체 문자열을 만들면 된다.

즉,

- `+=`는 계속 새 문자열을 만들 가능성이 크고
- `join()`은 마지막에 한 번 크게 합친다

는 차이가 있다.

그래서 chunk 수가 많아질수록 `join()` 쪽이 훨씬 유리해진다.


## 정리

이번 비교의 핵심은 단순하다.

- 문자열에 계속 `+=`를 하면 매번 새 문자열이 만들어질 수 있다.
- 리스트에 `append()`로 모아두고 마지막에 `join()` 하면 훨씬 효율적이다.
- 특히 chunk가 많아지는 스트리밍 환경에서는 이 차이가 더 분명해진다.

평소에는 사소해 보이지만,  
이런 작은 차이가 쌓이면 실제 응답 처리 코드의 성능과 구조가 꽤 달라진다.

그래서 문자열 조각을 많이 합쳐야 한다면,  
대부분의 경우 `+=`보다 `append() + join()`을 먼저 떠올리는 편이 좋다.

## 하.지.만
실시간 스트리밍 환경에서 실제로 100,000 토큰 이상의 문자열을
이어 붙일 일은 생각보다 많지 않다.

또한 대부분의 latency는 문자열을 합치는 비용보다는
LLM의 실제 generation 속도에 더 크게 영향을 받는다.

그래서 이 차이가 실제 서비스 성능에
큰 영향을 주지 않을 수도 있다.