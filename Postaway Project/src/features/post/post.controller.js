import PostModel from "./post.model.js";

export default class PostController{
    addPost(req, res){
        const { caption } = req.body;
        if(!req.file){
            return res.status(400).send({error: "File is not found"});
        }
        const file = req.file.filename;
        const userId = req.userId;
        const newPost = {
            userId,
            caption,
            imageUrl: file
        };
        console.log(newPost);
        const createdPost = PostModel.add(newPost);
        return res.status(201).send(createdPost);
    }
    updatePost(req, res){
        const { caption } = req.body;
        const id = req.params.id;
        let file = '';
        if(req.file){
            file = req.file.filename;
        }
        const userId = req.userId;
        const updatedPost = PostModel.update(id, userId, caption, file);
        if(updatedPost.success == false){
            return res.status(400).send(updatedPost);
        } else {
            return res.status(200).send(updatedPost);
        }
    }
    deletePost(req, res){
        const id = req.params.id;
        const userId = req.userId;
        const deletedPost = PostModel.delete(id, userId);
        if(deletedPost.success == false){
           return res.status(400).send(deletedPost);
        } else {
            return res.status(200).send(deletedPost);
        }
    }
    getAllPosts(req, res){
        const posts = PostModel.getAll();
        return res.status(200).send(posts);
    }
    getOneUserPosts (req, res){
        const userId = req.userId;
        const posts = PostModel.getUserPost(userId);
        if(posts.success == false){
            return res.status(400).send(posts);
        } else {
            return res.status(200).send(posts);
        }
    }
    getOnePost (req, res){
        const id = req.params.id;
        const userId = req.userId;
        const post = PostModel.getOne(id, userId);
        if(post.success == false){
            return res.status(400).send(post);
        } else{
            return res.status(200).send(post);
        } 
    }

    filterPosts(req, res){
        const caption = req.query.caption;
        const result = PostModel.filterData(caption);
        return res.status(200).send(result);
    }
    addPostDraft(req, res){
        const { caption } = req.body;
        if(!req.file){
            return res.status(400).send({error: "File is not found"});
        }
        const file = req.file.filename;
        const userId = req.userId;
        const newPost = {
            userId,
            caption,
            imageUrl: file
        };
        console.log(newPost);
        const createdPost = PostModel.addDraft(newPost);
        return res.status(201).send(createdPost);
    }
    sortPosts(req, res){
        const posts = PostModel.getAll();
        const sortedData = posts.sort((a,b)=> a.caption.localeCompare(b.caption));
        return res.status(200).send(sortedData);
    }
}