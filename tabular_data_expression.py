# 파이썬에서 표형 데이터(로우, 컬럼) 표현 방법
# --> 결과적으로 이중 리스트로 표현 (list of list)

product_list = [
    [1, '오리', 15000, 345],
    [2, '닭', 12000, 12323],
]

for product in product_list:
    print(product)