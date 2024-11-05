import CommentModel from "./comment.model.js";

export default class CommentController{
    getPostComments(req, res){
        const postId = req.params.postId;
        const commentList = CommentModel.getAll(postId);
        if(commentList.success == false){
            return res.status(400).send(commentList);
        } else {
            return res.status(200).send(commentList);
        }
    }
    addComment(req, res){
        const {postId, content} = req.body;
        const userId = req.userId;
        const comment = {
            userId,
            postId,
            content,
        }
        const addedComment = CommentModel.add(comment);
        return res.status(201).send(addedComment);
    }
    updateComment(req, res) {
        const {postId, content} = req.body;
        const userId = req.userId;
        const id = req.params.id;
        const updatedComment = CommentModel.update(id, userId, postId, content);
        if(updatedComment.success == false){
            return res.status(400).send(updatedComment);
        } else {
            return res.status(200).send(updatedComment);
        }
    }
    deleteComment(req, res){
        const id = req.params.id;
        const userId = req.userId;
        const deletedComment = CommentModel.delete(id, userId);
        if(deletedComment.success == false){
            return res.status(400).send(deletedComment);
        } else {
            return res.status(200).send(deletedComment);
        }
    }
}