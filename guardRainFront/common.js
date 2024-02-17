function login() {
  const id = document.querySelector('#ID');
  const pw = document.querySelector('#PW');

  if (id.value == "" || pw.value == "") {
    alert("로그인 할 수 없습니다.");
  } else {
    location.href = "main.html";
  }
}

function back() {
  history.go(-1);
}

function create_account() {
  const id = document.querySelector("#j_ID"); // 아이디
  const pw = document.querySelector("#join_pw"); // 패스워드
  const check_pw = document.querySelector("#check_pw"); // 패스워드 확인
  const pwMsg = document.querySelector("#pwMsg");

  regPw = /^[a-zA-Z].*[!@#$%^&*(),.?":{}|<>0-9].{4,}$/;

  if (id.value == "" || pw.value == "" || check_pw.value == "") {
    alert("회원가입을 할 수 없습니다.");
    return false; // 추가: 입력값이 누락되었을 경우 함수 종료
  }

  if (pw.value !== check_pw.value) {
    alert("비밀번호를 확인해주세요");
    return false; // 추가: 비밀번호가 일치하지 않을 경우 함수 종료
  }

  if (!regPw.test(pw.value)) {
    alert("비밀번호는 영어+숫자+특수문자가 포함되어야 합니다.");
    return false; // 추가: 비밀번호 규칙에 맞지 않을 경우 함수 종료
  }

  // 위에서 모든 검증이 통과하면 아래 코드가 실행됨
  location.href = "Login_Page.html";
}

// 아래에 추가: subm 버튼의 클릭 이벤트 핸들러 등록
document.querySelector('#subm').onclick = function () {
  if (id.value == "") {
    alert("아이디를 입력하세요");
    return false;
  }
};

document.querySelector("#check_pw").addEventListener("focus", function () {
  if (document.querySelector("#join_pw").value == "") {
    alert("패스워드를 먼저 입력하세요");
    document.querySelector("#join_pw").focus();
  }
});

document.querySelector("#subm").onclick = function () {
  if (pw.value == "") {
    alert("비밀번호를 입력하세요");
    return false;
  } else {
    if (!regPw.test(pw.value)) {
      alert("비밀번호는 영어+숫자+특수문자가 포함되어야 한다.");
      return false;
    }
  }
};

document.querySelector("#check_pw").addEventListener("blur", function () {
  if (document.querySelector("#join_pw").value != document.querySelector("#check_pw").value) {
    pwMsg.style.color = 'red';
    pwMsg.innerHTML = "일치하지 않습니다.";
    return false;
  } else if (document.querySelector('#join_pw').value == "") { }
  else {
    pwMsg.style.color = "green";
    pwMsg.innerHTML = "일치합니다.";
  }
});
