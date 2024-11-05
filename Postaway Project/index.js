import express from 'express';
import cookieParser from 'cookie-parser';
import swagger from 'swagger-ui-express';
import cors from 'cors';


import userRouter from './src/features/user/user.route.js';
import jwtAuth from './src/middlewares/jwt.middleware.js';
import postRouter from './src/features/post/post.route.js';
import commentRouter from './src/features/comment/comment.route.js';
import likesRouter from './src/features/like/likes.route.js';
import { ApplicationError } from './src/error-handler/applicationError.js';
import loggerMiddleware from './src/middlewares/logger.middleware.js';
import apiDocs from "./swagger.json" assert {type: 'json'}; 

const server = express();

// CORS Policy Configuration
var corsOptions = {
    origin: ['http://localhost:3000']
    // allowedHeaders
}
server.use(cors(corsOptions));

server.use(express.json());
server.use("/api-docs", swagger.serve, swagger.setup(apiDocs));
server.use(cookieParser());
server.use(loggerMiddleware);

server.use('/api/user', userRouter);
server.use('/api/posts', jwtAuth, postRouter);
server.use('/api/comments', jwtAuth, commentRouter);
server.use('/api/likes', jwtAuth, likesRouter);

//3. default request handler
server.get('/',(req,res)=>{
    res.send("Welcome to Postaway Project !!!");
});


// Middleware to handle default requests
server.use((err, req, res, next)=>{
    console.log(err);
    if(err instanceof ApplicationError ){
        res.status(err.code).send(err.message);
    }
    //Server Errors
    res.status(500).send('Something Went Wrong, Please try later');
});

server.use((req, res)=>{
    res.status(404).send("API Noe Found, Please check our documentation for more information at http://localhost:3200/api-docs");
});

server.listen(3000, ()=>{
    console.log("SERVER IS RUNNING ON PORN NUMBER 3000");
});