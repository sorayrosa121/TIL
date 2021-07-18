# 2021-07-16



## Git Branch





### master branch에서 파일 작성 후 commit



- branch 생성 전, "master" branch에서 day1.txt 파일 작성

  ```bash
  # "master" branch에서
  # username@DESKTOP MINGW64 ~/Desktop/foldername (master)
  
  
  touch day1.txt # day1.txt 파일 생성
  git init # 해당 폴더에 .git 시작
  ```





- git 상태 확인

  ```bash
  git status # On branch master
  ```

  > On branch master
  >
  > No commits yet
  >
  > Untracked files:
  >   (use "git add <file>..." to include in what will be committed)
  >         day1.txt
  >
  > nothing added to commit but untracked files present (use "git add" to track)





- 변동 사항 git add 후 commit

  ```bash
  git add .
  git commit -m "day1.txt created on branch master"
  ```

  



### 새로운 branch 만들기



- 새로운 이름의 branch 생성 (ex. rosa)

  ```bash
  git branch "rosa" # (큰 따옴표 표기 안 함)
  ```





- "rosa" branch로 전환

  ```bash
  git checkout "rosa" # (큰 따옴표 표기 안 함)
  ```

  > Switched to branch 'rosa'





- 새로 생성된 "rosa" branch에서 day2.txt 파일 작성 후 add, commit

  ```bash
  # "rosa" branch에서
  # username@DESKTOP MINGW64 ~/Desktop/foldername (rosa)
  
  
  touch day2.txt # day2.txt 파일 생성
  git add .
  git commit -m "day2.txt created on rosa branch"
  ```





- rosa branch에서 log 확인

  ```bash
  git log --oneline # git log를 간략하게 한 줄로
  ```

  > cba4321 (HEAD -> rosa) day2.txt created on rosa branch
  >
  > 1234abc (master) day1.txt created on branch master





- master branch로 전환한 후, log 확인

  ```bash
  git checkout master
  git log --oneline
  ```

  > 1234abc (HEAD -> master) day1.txt created on branch master

  > rosa branch에서 작성 후 commit한 day2.txt 로그내역은 아직 없음





- rosa branch를 master branch에 merge

  ```bash
  git merger rosa
  ```

  > Updating 1234abc..cba4321
  > Fast-forward
  >  day2.txt | 0
  >  1 files changed, 0 insertions(+), 0 deletions(-)
  >  create mode 100644 day2.txt





- master branch의 log 다시 한 번 확인

  ```bash
  git log --oneline
  ```

  >cba4321 (HEAD -> master, rosa) day2.txt created on rosa branch
  >
  >1234abc (master) day1.txt created on branch master





### branch 삭제하기



- "rosa" branch 삭제

  ```bash
  git branch -d "rosa" # (큰 따옴표 표기 안 함)
  ```





- 남은 branch 확인

  ```bash
  git branch
  ```

  > * master



