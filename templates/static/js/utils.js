/**Utility Scripts */
function fetchTodos() {
  /*Fetch Sample Todos for Home Page */
  getRequest(getTodosPageOne, "", updateIndexHtml);
}

function updateIndexHtml(content) {
  console.log(content);
  sampleGetRequest.innerHTML = content;
}
