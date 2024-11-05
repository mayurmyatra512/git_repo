import LikesModel from "./like.model.js";

export default class LikesController{
    getAllLikesPost(req, res){
        const postId = req.params.postId;
        const userId = req.userId;

        const likedData = LikesModel.getAll(postId);
        if(likedData.success == false){
            return res.status(404).send(likedData.msg);
        } else {
            return res.status(200).send(likedData);
        }
    }

    likesOperations(req, res){
        const postId = req.params.postId;
        const userId = req.userId;

        const result = LikesModel.addRemoveLikes(userId, postId);
        return res.status(200).send(result);
    }
}