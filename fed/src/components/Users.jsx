import React from "react";
import User from "./User";


const Users = ({ users, handleDone, handleMoreDetail, handleAddTodo }) => {
  
  return (
    <ul className="list-group list-group-flush">
      {users.map(user => (
        <User
          key={user.id}
          user={user}
          handleDone={handleDone}
          handleMoreDetail={handleMoreDetail}
        />
      ))}
      {/* <AddTodo handleAddTodo={handleAddTodo} /> */}
    </ul>
  );
};

export default Users;
