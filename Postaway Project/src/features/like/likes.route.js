import LikesController from "./likes.controller.js";
import express from 'express';
// import postIdValid from '../../middlewares/validPostId.middleware.js';

const likesRouter = express.Router();
const likesController = new LikesController();

// All the Paths to Controller Method
//Get
likesRouter.get('/:postId', likesController.getAllLikesPost);
likesRouter.get('/toggle/:postId', likesController.likesOperations);


export default likesRouter;