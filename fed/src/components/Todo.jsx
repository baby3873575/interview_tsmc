import React from "react";


const Todo = ({ todo, handleDone }) => {
  return (
    <li className="list-group-item d-flex align-items-baseline list-unstyled">
      <input
        type="checkbox"
        id={"done" + todo._id}
        className="mr-4"
        onChange={() => handleDone(todo)}
        defaultChecked={todo.completed}
      />
      <label for={"done" + todo.id}>
        {todo.completed ? <s>{todo.title}</s> : todo.title}
      </label>
    </li>
  );
};

export default Todo;
