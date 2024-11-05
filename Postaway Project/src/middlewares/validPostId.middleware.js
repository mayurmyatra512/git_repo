import PostModel from "../features/post/post.model.js";

const postIdValid = (req, res, next)=>{
    const {postId} = req.body;
    console.log(postId)
    const validity = PostModel.checkPostId(postId);
    console.log(validity)
    if(!validity){
        return res.status(404).send("Please Enter valid postId");
    }
    next();
}

export default postIdValid;