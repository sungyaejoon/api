async function callAPI() {

    const name = document.getElementById("nameInput");
    const response = await fetch(`http://127.0.0.1:5001/hello?name=${name}`);
    const data = await response.json();
    document.getElementById("result").innerText = data.message;
}