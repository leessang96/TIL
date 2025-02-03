..0# 250131_강의

# 딕셔너리

1. 키 - 값으로 쌍을 이루고 있다.
2. 순서가 없다.
3. {}로 만든다.
4. 키는 고유해야한다.
    - 키는 immutable한 타입만 올 수 있다. (ex : 문자열, 리스트 등등)
5. 값은 어떤 것도 다 허용
6. 가변형

## 딕셔너리 생성

```python
my_dict = {}
my_dict2 = dict() # 빈 딕셔너리를 반환 return {}

my_dict3 = {'nave' : 'Alice', 'age' : 25} # 초기화 (초기값을 준 상태로)
my_dict3.clear() # {} 빈 딕셔너리 출력

# .get(key[, default]) 메서드 
# 메서드 안의 대괄호[]는 없어도 되는 구문이라 선택사항 같은 느낌이라 보면 됨
my_dict3.get('name') # Alice

# key(), values(), items() 들의 공통점 : 딕셔너리에 있는 특별한 view 객체
# 원본 객체의 실시간 상태를 반영해서 보여줍니다.
person = {'name' : 'Alice', 'age' : 25, 'gender' : 'Female'}
person.keys()   # 'name, 'age', 'gender'
person.items()  # [('name', 'Alice'), ('age', 25), ('gender', 'Female')]
person.values() # ['Alice', 25, 'Female']

type(person.keys())     # <class 'dict_keys'>
type(person.items())    # <class 'dict_items'>
type(person.values())   # <class 'dict_values'>

# .pop(key[, default]) : 키를 제거하고 연결됐던 값을 반환(없으면 에러나 default를 반환)
person.pop('name') # {'age' : 25, 'gender' : 'Female'}

# .setdefault(key[, default]) : 키와 연결된 값을 반환 (키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환)
student = {'name' : 'isaac'}
student.setdefault('age', 20)   # {'name' : 'isaac', 'age' : 20}

# .update([other]) : other가 제공하는 키/값 쌍으로 딕셔너리를 갱신, 기존 키는 덮어씀
person = {'name' : 'Alice', 'age' : 25, 'gender' : 'Female'}
other_person = {'name' : 'Jane', 'country' : 'KOREA'}
person.update(other_person) # {'name' : 'Jane', 'age' : 25, 'country' : 'KOREA'}
```

---

# Set

1. 중복 없음
2. 순서 없음
3. 해시가 가능한 객체만 담을 수 있다.
4. Mutable

## 세트 생성
```python

my_set = {'a', 'b', 'c', 1, 2, 3}
my_set1 = set()
my_set2 = set([1, 2, 3, 4])

# .add(x)
my_set.add('d')     # {1, 2, 3, 'b', 'd', 'a', 'c'}

# .clear() : 세트의 모든 항목 제거
my_set.clear()      # set() / 중괄호로 출력되지 않는 이유는 딕셔너리와 구분짓기 위함

# .remove(x) : 세트에서 항목 x를 제거
my_set.remove('d')  # {1, 2, 3, 'b', 'a', 'c'}

# .pop() : 세트에서 임의의 요소를 제거하고 반환
el = my_set.pop()   # 랜덤한 요소가 삭제됨

# .discard() : 세트 s에서 항목 x를 제거, remove와 달리 에러 없음
my_set.discard(2)   # {1, 3, 'b', 'c', 'a'}
my_set.discard(10)  # 에러 안남

# .update(iterable) : 세트에 다른 iterable 요소를 추가
my_set.update([1,4,5])  # {'b', 1, 2, 3, 'c', 4, 5, 'a'}

```

---

# 해시 테이블
- 해시 함수를 사용하여 변환한 값을 인덱스로 삼아 키와 데이터를 저장하는 자료구조
    -> 데이터를 빠르게 저장하고 검색하기 위해 사용

    ## 원리
    1. 키를 해시 함수를 통해 해시 값으로 변환
    2. 변환된 해시 값을 인덱스로 삼아 데이터를 저장하거나 찾음
    3. 검색, 삽입, 삭제가 매우 빠르게 수행
    - 충돌 확률 낮추기 위해 단순화 하지 않음

    ## set의 요소 & dictionar의 키와 해시테이블 관계
    - set
        - 각 요소를 해시 함수로 변환해 나온 해시 값을 맞춰 해시 테이블 내부 버킷에 위치
        - '순서'라기보다 '버킷 위치(인덱스)' 가 요소의 위치를 결정
        - 따라서 set는 순서를 보장하지 않음
    
    - dict
        - 키(key) -> 해시 함수 -> 해시 값 -> 해시 테이블에 저장
        - set와 달리 '삽입 순서' 는 유지한다는 것이 언어 사양으로 보장 됨
        - 키를 추가한 순서대로 반복문 순회할 때 나오게 됨
        - 사용자에게 보여지는 키 순서는 삽입 순서가 유지되도록 설계된것

    ## hashable
    - hash() 함수에 넣어 해시 값을 구할 수 있는 객체를 의미
    - 대부분의 불변 타입은 해시 가능 ( int, float, str, tuple) 
    - 가변형 객체(list, dict, set)는 기본적으로 해시 불가능
        - 