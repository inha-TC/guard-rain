function login(){
  const id = document.querySelector('#ID');
  const pw = document.querySelector('#PW');

  if (id.value == "" || pw.value == ""){
    alert("로그인 할 수 없습니다.")
  } 
  else {
    location.href = "main.html";
  }
}

function back() {
  history.go(-1);
}

function create_id() {
  const id = document.querySelector("#j_ID");
  const pw = document.querySelector("#j_PW");
  const r_pw = document.querySelector("#Check_PW");

  if (id.value == "" || pw.value == "" || r_pw == ""){
    alert("회원가입을 할 수 없습니다.")
  }
  else {
    if (pw.value !== r_pw.value){
      alert("비밀번호를 확인해주세요")
    } else {
      location.href = "Login_Page.html";
    }
  }
}