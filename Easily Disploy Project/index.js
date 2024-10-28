import express from 'express';
import ejsLayouts from 'express-ejs-layouts';
import path from 'path';
import JobController from './src/controllers/job.controller.js';
import { uploadFile } from './src/middlewares/upload.middleware.js';
import UserController from './src/controllers/user.controller.js';
import { auth } from './src/middlewares/auth.middleware.js';
import session from 'express-session';
import validateRequest from './src/middlewares/validate.middleware.js';
import cookieParser from 'cookie-parser';
import { setLastVisit } from './src/middlewares/lastvisit.middleware.js';



const app = express();

// let staticPath = path.join('EASILY DISPLOY PROJECT','public');
app.use(express.static('public'));

app.use(cookieParser());
app.use(setLastVisit);

app.use(session({
  secret: 'SecretKey',
  resave: false,
  saveUninitialized: true,
  cookie: { secure: false },
}))

const jobController = new JobController();
const userController = new UserController()

app.use(ejsLayouts);
app.use(express.json());

app.use(express.urlencoded({ extended: true }));
// app.use('/src/uploads', express.static('uploads'));

app.set('view engine', 'ejs');
app.set(
  'views',
  path.join(path.resolve(), 'src', 'views')
);


app.get('/', jobController.getLanding);

app.get('/jobs', jobController.getJobList);

app.get('/job/:id', jobController.getJobDet);

app.post('/apply/:id',uploadFile.single('resume'), jobController.postApply);
app.get('/applicants/:id', auth,uploadFile.single('resume'), jobController.getApplicants);
app.get('/src/uploads/:filename',auth, jobController.getFile);

app.get('/postjob', auth, jobController.getAddJob);

app.get('/job/update/:id', auth, jobController.getUpdateJob);
app.post('/job/update/:id', auth, jobController.postUpdateJob);
app.post('/job/delete/:id', auth, jobController.postDeleteJob);
app.post('/job/add', auth, validateRequest, jobController.postAddJob);
app.post('/search', jobController.postSearchJob);

app.post('/register', userController.postRegister);

app.get('/login',userController.getLogin);

app.post('/login', userController.postLogin);

app.get('/logout', userController.logout)

app.listen(3500, () => {
    console.log('Server is running on port 3500');
  });


