# 2021-07-15



## CLI (Command Line Interface)



### Command 관련

- 과거 명령어 불러오기(위, 아래 방향키)

- 자동 완성(tab)

- `ctrl + a`: 커서가 맨 앞으로 이동

- `ctrl + e`: 커서가 맨 뒤로 이동

- `ctrl + w`: 커서 앞 단어 지우기

- ">" 에 갇혔을 때는 `Ctrl + C`를 누르세요.

- Ctrl+C, Ctrl+V 하는 방법

  > Ctrl + insert, Shift + insert



## 경로

- 현재 경로, 즉 파일이나 폴더의 고유한 위치를 나타내는 문자열 (주소)
  - windows) C:\Users\Document
  - macOS) /User/Document

  

### **루트 디렉토리**

- 모든 파일/폴더를 담고 있는 폴더
- windows의 경우 보통 C 드라이브를 의미



### **상대 경로**

- 현재 워킹 디렉토리를 기준으로 계산된 경로
- 현재 워킹 디렉토리가 `C:\\Users\\User\\바탕 화면` 라면, `C:\\Users\\USER\\바탕 화면\\code`의 상대 경로는 `"code"` 가 된다.



### **`~` 틸드(Tilde)**

- 현재 사용자의 홈 디렉토리를 의미
- 현재 사용자란, 컴퓨터에 로그인 하는 계정



## Command



### cd

- 경로 이동 (Change Directory)
- 현재 워킹 디렉토리를 변경하기 위해 사용
- `cd ..` 는 부모 폴더
- `cd .` 는 현재 폴더



### pwd

- 현재 작업중인 폴더(디렉토리)



### ls

- 현재 워킹 디렉토리의 폴더/파일 확인

- Git Bash 실행 -> `$ pwd` -> `$ ls -al`
- `로컬 디스크(C:)` -> `사용자` -> `"user name"` 클릭하여 GUI로 확인 가능



### touch

- `touch a.txt` 형식으로 **파일** 생성



### mkdir

- `mkdir "디렉토리 이름"` 형식으로 **폴더** 생성

- `mkdir happy hacking`의 경우, 'happy' 와 'hacking' 이라는 폴더 2개가 만들어짐

  > `mkdir 'happy_hacking'` 으로 생성 필요



### rm

- 파일 삭제

- `rm -r` 폴더 삭제

- cp, mv

  - 복사 (복사, 붙여넣기)

    ```bash
    $ cp a.txt b.txt
    $ cp a.txt aa.txt
    ```

  - 이동 (잘라내기, 붙여넣기)

    ```bash
    $ mv b.txt b/b.txt
    ```

- 이름 바꾸기

  ```bash
  $ mv aa.txt c.txt
  ```



## Vi 에디터

- bash 내 vi 로 진입
- vi a.txt로 파일 작성 가능

> 편집모드 (i)

> 일반모드(esc)

> 저장 후 나가기(:wq) 
