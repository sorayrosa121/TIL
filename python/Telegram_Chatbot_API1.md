# 	2021-07-16



## 텔레그램 챗봇 API 활용하기 1



### Token 받기



1. BotFather 검색 (@BotFather)

2. 시작 버튼 (/start)

3. 하단과 같은 말풍선에서 /newbot 선택 OR 채팅창에 "/newbot" 입력 (큰 따옴표 표기 안 함)

    ```
    I can help you create and manage Telegram bots. If you're new to the Bot API, please see the manual (https://core.telegram.org/bots).
    
    You can control me by sending these commands:
    
    /newbot - create a new bot
    /mybots - edit your bots [beta]
    
    Edit Bots
    /setname - change a bot's name
    /setdescription - change bot description
    /setabouttext - change bot about info
    /setuserpic - change bot profile photo
    /setcommands - change the list of commands
    /deletebot - delete a bot
    
    Bot Settings
    /token - generate authorization token
    /revoke - revoke bot access token
    /setinline - toggle inline mode (https://core.telegram.org/bots/inline)
    /setinlinegeo - toggle inline location requests (https://core.telegram.org/bots/inline#location-based-results)
    /setinlinefeedback - change inline feedback (https://core.telegram.org/bots/inline#collecting-feedback) settings
    /setjoingroups - can your bot be added to groups?
    /setprivacy - toggle privacy mode (https://core.telegram.org/bots#privacy-mode) in groups
    
    Games
    /mygames - edit your games (https://core.telegram.org/bots/games) [beta]
    /newgame - create a new game (https://core.telegram.org/bots/games)
    /listgames - get a list of your games
    /editgame - edit a game
    /deletegame - delete an existing game
    ```

4. 하단의 말풍선에 대해, 채팅 봇의 이름 입력 (ex. rosa)

   ```
   Alright, a new bot. How are we going to call it? Please choose a name for your bot.
   ```

   

5. 하단의 말풍선에 대해, 채팅 봇의 user name 입력. 단, "_bot"으로 끝내야 함 (ex. rosa_bot)

   ```
   Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.5-1. 
   ```

   > `Sorry, this username is already taken. Please try something different.` 라고 뜨는 경우, 중복된 user name이 존재하므로, 새롭게 입력해야함



6. 하단의 말풍선 마지막 줄에서 https://core.telegram.org/bots/api 을 클릭하거나, 해당 URL로 진입하여 api document를 확인

   ```
   Done! Congratulations on your new bot. You will find it at t.me/rosarosa_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
   
   Use this token to access the HTTP API:
   ##### 이 곳에 사용 가능한 token이 주어집니다 #####
   Keep your token secure and store it safely, it can be used by anyone to control your bot.
   
   For a description of the Bot API, see this page: https://core.telegram.org/bots/api
   ```



7. 동시에, 상단의 말풍선에서 밑에서 3번째 줄에 주어진 개인별 token을 텍스트 파일에 저장해두거나, 코드 내 변수 값으로 입력한다.

   ```python
   # 토큰은 개인별로 다르게 주어지며 하단의 토큰은 임의로 작성한 예시
   
   token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
   ```





### URL로 확인하기



1. api document 오른쪽 목차의 "authorizing-your-bot" 클릭, 혹은 https://core.telegram.org/bots/api#authorizing-your-bot



2. "Making requests" 의 파란색으로 표시된 API 쿼리를 복사하고, "<token>" 부분에 **7.** 에서 저장한 토큰 값을 입력

   ```python
   ### https://api.telegram.org/bot<token>/METHOD_NAME 의 형태
   ```

   

3. getMe의 입력 예시와 결괏값 (id 확인)

   `https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` `/getMe`

   ```json
   // 20210716094642
   // https://api.telegram.org/bot### 입력한 개인 token ###/getMe
   
   {
     "ok": true,
     "result": {
       "id": ### 이 곳에 id가 주어집니다 ###,
       "is_bot": true,
       "first_name": "### 챗봇의 이름 ###",
       "username": "### 챗봇의 user name ###",
       "can_join_groups": true,
       "can_read_all_group_messages": false,
       "supports_inline_queries": false
     }
   }
   ```

   > id 확인 후 저장



4. getUpdates의 입력 예시와 결괏값

   `https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` `/getUpdates`

   ```json
   // 20210716094909
   // https://api.telegram.org/bot### 입력한 개인 token ###/getUpdates
   
   {
     "ok": true,
     "result": [
       
     ]
   }
   ```

   > 아직 대화 내역이 없으므로, result 가 비어있음



5. sendMessage의 입력 예시와 결괏값

   ```
    api document를 살펴보면, "chat_id"와 "text" 변수(parameter)의 required가 'Yes'이므로 필수로 작성한다
   ```

   `https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` `/sendMessage` `?chat_id=` `<개인 id>` `&text="하고싶은 말"`

   > 화살 괄호(<>), 큰 따옴표("") 표기 안 함

   

   ```json
   {
     "ok": true,
     "result": {
       "message_id": 4,
       "from": {
         "id": ### 개인 id ###,
         "is_bot": true,
         "first_name": "### 챗봇의 이름",
         "username": "### 챗봇의 user name ###"
       },
       "chat": {
         "id": ### 개인 id ###,
         "first_name": "### 이름 ###",
         "type": "private"
       },
       "date": 1626397869,
       "text": "하고싶은 말"
     }
   }
   ```

   