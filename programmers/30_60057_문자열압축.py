def solution(s):
    # 5번 테스트 케이스 예외처리
    if len(s) == 1:
        return 1

    candidate = []

    # 주어진 문자열을 절반으로 자르는게 word의 최대치 (abcabc -> 2abc)
    # 자르는 단위를 1부터 len(s) // 2 까지 시도
    for cut in range(1, len(s) // 2 + 1):
        # print("cut", cut)
        compressed = ""

        word = s[:cut]  # cut이 1일때 word = "a", 2일때 "ab", 3일때 "abc"
        # print("word", word)
        count = 1

        for i in range(cut, len(s), cut):
            next_word = s[i:i + cut]

            if word == next_word:
                count += 1
            else:
                # 단어 반복 끝 -> 다음 단어 반복
                if count != 1:
                    compressed += str(count)

                compressed += word
                word = s[i:i + cut]
                # print("word", word)
                count = 1

        # 마지막 단어는 따로 붙여줌
        # 마지막 단어가 딱 떨어지는 경우: count가 1이상 붙어서 출력 ex) aabbcc -> 2c, aabbcccc -> 2cc
        # 마지막 단어가 자투리인 경우: count가 무조건 1 -> 그냥 단어만 출력 ex) aabbc -> c
        if count != 1:
            compressed += str(count)

        compressed += word

        # print("compressed", compressed)
        # print("-----------")
        candidate.append(len(compressed))

    # print("candidate", candidate)
    return min(candidate)


# print("result", solution(input()))
