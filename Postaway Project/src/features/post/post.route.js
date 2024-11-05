import express from "express";
import PostController from "./post.controller.js";
import { upload } from "../../middlewares/fileupload.middleware.js";

const postRouter = express.Router();
const postController = new PostController();

// All the Paths to Controller Method
// GET
postRouter.get('/all', postController.getAllPosts);
postRouter.get('/', postController.getOneUserPosts);
postRouter.get('/:id', postController.getOnePost);
postRouter.get('/filter', postController.filterPosts);
postRouter.get('/sort', postController.sortPosts);
//POST
postRouter.post('/', upload.single('imageUrl'), postController.addPost);
//PUT
postRouter.put('/:id',upload.single('imageUrl'), postController.updatePost);
//DELETE
postRouter.delete('/:id', postController.deletePost)

export default postRouter;