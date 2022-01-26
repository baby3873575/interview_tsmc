import React from "react";


const Comment = ({comment}) => {
  
  return (
      <><p><span class="badge badge-secondary">{comment.email}</span>: {comment.body}</p><hr></hr></>
  );
};

export default Comment;

