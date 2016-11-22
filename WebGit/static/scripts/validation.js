function validate_repository	(url)
{
// 1. Создаём новый объект XMLHttpRequest
var xhr = new XMLHttpRequest();
// 2. Конфигурируем его: GET-запрос на URL 'phones.json'
xhr.open('GET', 'https://api.github.com/repos/KosoFF/flask', false);
// 3. Отсылаем запрос
xhr.send(null);
if (xhr.readyState == 4 && xhr.status == 200) {
    var response = JSON.parse(xhr.responseText);
    alert(response);
    document.getElementById('validation_result').innerHTML = xhr.responseText;
}
    else
    {
        alert('Something is wrong')
    }

}