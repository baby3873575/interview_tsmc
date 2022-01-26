import React from "react";
import Comment from "./Comment";

const Post = ({post,key}) => {
  
  return (
    <div class="card">
      <div class="card-header" id={ 'heading' + key }>
        <h5 class="mb-0">
          <button class="btn " type="button" data-toggle="collapse" data-target={ '#collapse' + key } aria-expanded="true" aria-controls={ 'collapse' + key }>
            {post.body}
          </button>
        </h5>
      </div>

      <div id={ '#collapse' + key } class="collapse show" aria-labelledby={ 'heading' + key } data-parent="#accordionExample">
        <div class="card-body">
          <h6>Comments</h6>
          {post.comments.map(comment => (
            <Comment
              comment={comment}
            />
          ))}
        </div>
      </div>
    </div>

  );
};

export default Post;

