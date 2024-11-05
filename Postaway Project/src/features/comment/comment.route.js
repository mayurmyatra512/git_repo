import express from 'express';
import CommentController from "./comment.controller.js";
import postIdValid from '../../middlewares/validPostId.middleware.js';

const commentRouter = express.Router();
const commentController = new CommentController();

// All the Paths to Controller Method
//GET
commentRouter.get('/:postId', commentController.getPostComments);
//POST
commentRouter.post('/', postIdValid, commentController.addComment);
//PUT
commentRouter.put('/:id', postIdValid, commentController.updateComment);
//DELETE
commentRouter.delete('/:id', commentController.deleteComment);

export default commentRouter;