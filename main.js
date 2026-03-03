function askName() {
  const name = prompt("이름이 뭐야?");
  if (name) {
    document.getElementById("result").innerText = "내 이름은 김민곤이야";
  }
}