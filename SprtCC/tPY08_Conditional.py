# 조건문 - Conditional Statements

def oddeven(num):  # oddeven이라는 이름의 함수를 정의한다. num을 변수로 받는다.
	if num % 2 == 0:  # num을 2로 나눈 나머지가 0이면
	 return True   # True (참)을 반환한다.
	else:            # 아니면,
	 return False  # False (거짓)을 반환한다.


result = oddeven(20)
# result의 값은 무엇일까요?
print("result = oddeven(20):", result)


def is_adult(age):
	if age > 20:
		print('성인입니다')    # 조건이 참이면 성인입니다를 출력
	else:
		print('청소년이에요')  # 조건이 거짓이면 청소년이에요를 출력


# 무엇이 출력될까요?
print("is_adult(30):", is_adult(30))
