import jwt from 'jsonwebtoken';

import UserModel from "./user.model.js";

export default class UserController{
    getUser(req, res){
        const user = UserModel.getAll();
        res.status(200).send(user);
    }
    signUp(req, res){
        const { name, email, password } = req.body;
        const addedUser = UserModel.signup(name, email, password);
        res.status(201).send(addedUser);
    }

    log_in(req, res){
        console.log(req.body);
        const {email, password} = req.body;
        const user = UserModel.login(email, password);
        if(user.status ==false){
            return res.status(400).send("Incorrect Credentials");
        } else {
            console.log(user.msg.email);
            // return res.status(200).send(user);
            //1. Create Token
            const token = jwt.sign({userID: user.msg.id, email: user.msg.email}, "MwRyYnzzcYlFEAkuhB9s3yoYt2oLYVGC", {expiresIn: '1h'});
            // res.cookie('jwtToken', token, {httpOnly: true, secure: true});
            //2. Send Token
            return res.status(200).cookie('jwtToken', token, {httpOnly: true, secure: true}).cookie("userId", user.msg.id, { maxAge: 900000, httpOnly: false }).send({Token: token, User: user});
        }
    }
}