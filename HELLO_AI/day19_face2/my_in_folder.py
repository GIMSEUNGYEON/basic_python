import os
path = "img"

files = os.listdir(path)
print(files) 

for idx, file in enumerate(files):
    str_cnt = str(idx+100)[1:3]
    print("{{'lbl':'{}', 'f':'{}', 'n':'{}'}},".format(idx,str_cnt,file.replace(".mp4","")))
    # if idx < 10 :
    #     os.mkdir("pre01/0{}".format(idx))
    # else :
    #     os.mkdir("pre01/{}".format(idx))
    #

    # idx += 100
    #
    # print(str(idx)[1:])
    
# 0 김민경
# 1 김승연
# 2 김차은
# 3 김창용
# 4 김초희
# 5 김현우
# 6 남희수
# 7 박주호
# 8 박지원
# 9 배유림
# 10 백영웅
# 11 변상원
# 12 송은비
# 13 우민규
# 14 유길상
# 15 이미소
# 16 이상철
# 17 이성휘
# 18 정민지
# 19 하예종
