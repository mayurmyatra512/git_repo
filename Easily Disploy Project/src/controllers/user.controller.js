import JobModel from "../models/job.model.js";
import UserModel from "../models/user.model.js";


export default class UserController{

    getLogin(req, res){
        res.render('login');
    }

    postRegister(req,res){
        const {username, email, password } = req.body;
        UserModel.add(username, email, password );   
        res.render('login');
    }
    postLogin(req, res,next){
        const {email, password} = req.body;
        const user = UserModel.check(email, password);
        // console.log(user);
        if (!user) {
            return res.render('404_page', {
              errorMessage: 'User Not Found Please Register',
            });
          }
          req.session.userEmail = email;
          var jobs = JobModel.getAll();
          if(req.session.userEmail){
            res.render('jobListing', {jobs, userEmail: req.session.userEmail});
        }
        else{
            res.render('jobListing', {jobs, userEmail: null});
        }
    }

    logout(req, res){
        // on logout need to destroy the session
        req.session.destroy((err)=>{
            if(err){
                console.log(err);
            } else {
                res.redirect('/login');
            }
        })
        res.clearCookie('lastVisit');
    }
}