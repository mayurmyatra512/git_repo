export default class LikesModel{
    constructor(id, userId, postId){
        this.id = id;
        this.userId = userId;
        this.postId = postId;
    }
    static getAll(postId){
        const likedPosts =  likes.filter((l)=> l.postId == postId);
        if(!likedPosts){
            return {success: false, msg:"No Likes available for this postId"}
        }
        else{
            return {success:true, msg: likedPosts};
        }
    }
    static addRemoveLikes(userId, postId){
        const likesData = likes.filter(l => l.postId == postId && l.userId == userId)
        console.log(likesData);
        if(likesData.length != 0){
            const index = likes.findIndex((li)=> li.id == likesData.id)
            likes.splice(index, 1);
            return {success:true, msg:"Like removed from the post"}
        }
        const id = likes.length + 1;
        const newLikes = new LikesModel(id, userId, postId);
        likes.push(newLikes);
        return {success:true, msg: newLikes};
        
    } 
}

var likes = [
    new LikesModel(1, 1, 1)
]