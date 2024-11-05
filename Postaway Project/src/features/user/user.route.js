import express from 'express';
import UserController from "./user.controller.js";

const userRouter = express.Router();
const userController = new UserController();

// All the Paths to Controller Method
userRouter.get('/', userController.getUser);
userRouter.post('/signup', userController.signUp);
userRouter.post('/login', userController.log_in);

export default userRouter;