"""module docstring"""
import operator #모듈(계산할때 빠르게 하기 위해서 사용하는 모듈)
import sys #인수 전달(일단 그렇다고만 알아둔다)

def main(): #이게 이제 def합니다 라는 뜻 if main 있어야 읽어짐

    book_data = [] #비어있는 리스트 만드는 것

    with open(sys.argv[1], "r", encoding="utf8") as book: #[1]뜻은 이 파일 전체를 사용한다는 뜻, utf8인코딩 방식
        lines = book.readlines()

        for i in lines:
            temp = i.split('|') # |로 나눈다
            temp[1] = int(temp[1]) #temp 인덱스 1을 보거라
            temp[2] = temp[2].replace("\n", "") 
            book_data.append(temp)

    code = []


    for i in book_data:
        if i[2] in code:
            continue
        code.append(i[2])
    code.sort()

    string = [[] for _ in range(len(code))]
    num = [[] for _ in range(len(code))]

    for i in book_data:
        for j in range(len(code)):
            if i[2] == code[j]:
                string[j].append(i[0])
                num[j].append(i[1])

    make_summary = ''
    make_text = ''
    for i in range(len(code)):
        temp_list = []
        avg = 0

        for j in range(len(string[i])):
            temp_list.append([string[i][j], num[i][j]])

        sort_list = sorted(temp_list, key=operator.itemgetter(1))
        min_str = len(sort_list[0][0])
        max_str = len(sort_list[0][0])
        min_index = 0
        max_index = 0
        for k in range(len(sort_list)):
            str_len = len(sort_list[k][0])
            avg += str_len
            if min_str > str_len:
                min_str = str_len
                min_index = k
            if max_str <= str_len:
                max_str = str_len
                max_index = k

        make_text += (code[i] + '\n')

        for lis in sort_list:
            make_text += (lis[0] + '\n')

        make_text += '-----\n'

        avg /= len(sort_list)
        make_summary += (code[i] + '\n' + 'Longest line (')
        make_summary += (str(sort_list[max_index][1]) + '): ')
        make_summary += (sort_list[max_index][0] + '\n')
        make_summary += ('Shortest line (')
        make_summary += (str(sort_list[min_index][1]) + '): ')
        make_summary += (sort_list[min_index][0] + '\n')
        make_summary += ('Average length: ' + str(round(avg)) + '\n\n')
    make_text = make_text[:-6]
    with open('novel_summary.txt', "w", encoding="utf8") as novel_summary:
        novel_summary.write(make_summary)
    with open('novel_text.txt', "w", encoding="utf8") as novel_text:
        novel_text.write(make_text)

if __name__ == "__main__":
    main()

