# 2021-07-15



## Git

```bash
git status

git log

git reflog

git checkout "git log 내역으로 확인한 돌아가고싶은 지점 문자열 일부"
```



### Repository?

> 폴더 내 `.git` 디렉토리 (숨긴 항목)



## 새 Repository 생성 후

```bash
git remote add origin "https:// 레포지토리 주소.git"
git remote -v # 등록된 원격저장소 목록 확인
```



- "Remote origin already exists" error

````bash
git remote set-url origin "https:// 레포지토리 주소.git"
````

---



- git push 중 발생한 에러

> $ git push

> fatal: You are not currently on a branch.
> To push the history leading to the current (detached HEAD)
> state now, use git push origin HEAD:<name-of-remote-branch>

```bash
git checkout master
```



```bash
git remote add origin "https:// 레포지토리 주소.git"
git branch -M main
git push -u origin main
```

