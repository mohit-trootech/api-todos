/**Utility Scripts */
function fetchTodos() {
  /*Fetch Sample Todos for Home Page */
  let getTodosUrl = document.getElementById("todosRequest").value;
  if (getTodosUrl) {
    getRequest(getTodosUrl, "", updateIndexHtml);
  } else {
    getRequest("/api/todos/", "", updateIndexHtml);
  }
}

function updateIndexHtml(content) {
  sampleGetRequest.innerHTML = JSON.stringify(content, undefined, 4);
}
