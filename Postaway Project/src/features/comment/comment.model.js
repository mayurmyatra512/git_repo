
export default class CommentModel{
    constructor(id, userId, postId, content){
        this.id = id;
        this.userId = userId;
        this.postId = postId;
        this.content = content;
    }

    static getAll(postId){
        const commentList = comments.filter((p)=> p.postId == postId);
        console.log(commentList);
        if(!commentList){
            return {success: false, data: 'No Comments Found'};
        } else {
            return {success: true, data: commentList};
        }
    }

    static add(comment){
        comment.id = comments.length + 1;
        comments.push(comment)
        return {success: true, msg:comments};
    }

    static update(id, userId, postId, content){
        const commentIndex = comments.findIndex((c)=> c.id == id && c.userId == userId && c.postId == postId);
        if(commentIndex != -1){
            comments[commentIndex].content = content;
            return {success:true, msg:comments[commentIndex]};
        } else {
            return {success: false, msg: 'Please Enter valid ID !!!'};
        }
    }

    static delete(id, userId){
        const commentIndex = comments.findIndex((c)=> c.id == id && c.userId == userId);
        if(commentIndex == -1){
            return {success:false, msg: "operation not allowed"};
        } else {
            const deletedItem = comments.splice(commentIndex, 1);
            return {success: true, msg:'1 Comment deleted'}
        }
    }
}

var comments = [
    new CommentModel(
        1,
        1,
        1,
        'Wow!, This is the great Image...',
    )
]