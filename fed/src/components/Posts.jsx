import React from "react";
import Post from "./Post";

const Posts = ({ posts}) => {

  return (
    <><h4>Posts</h4><div class="accordion" id="accordionExample">
      {posts.map(post => (
        <Post
          key={post._id}
          post={post} />
      ))}
    </div></>
  );
};

export default Posts;

