import React from "react";
import Todo from "./Todo";

const Todos = ({ todos, handleDone }) => {
  return (
    <><h4 class="m-3"> Todos:</h4><ul className="list-group list-group-flush">
      {todos.map(todo => (
        <Todo
          key={todo.id}
          todo={todo}
          handleDone={handleDone} />
      ))}
    </ul></>
  );
};

export default Todos;
