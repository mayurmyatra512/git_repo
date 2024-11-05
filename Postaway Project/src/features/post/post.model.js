
export default class PostModel {
    constructor(id, userId, caption, imageUrl){
        this.id = id;
        this.userId = userId;
        this.caption = caption;
        this.imageUrl = imageUrl;
    }

    static getAll(){
        return {success:true, data: posts};
    }

    static getUserPost(userId){
        const userPosts = posts.find((p)=>p.userId == userId);
        console.log(userPosts)
        if(!userPosts){
            return {success: false, data: 'No Data Found'};
        } else {
            return {success: true, data: userPosts};
        }
    }

    static getOne(id, userId){
        const post = posts.find((p)=>p.id == id && p.userId == userId);
        if(!post){
            return {success: false, data: 'No Data Found, You can Access only Your Post !!!'};
        } else {
            return {success: true, data: post};
        }
    }

    static add(post){
        post.id = posts.length + 1;
        posts.push(post)
        return {success: true, msg:'Post Added Sccessfully !!!'};
    }

    static update(id, userId, caption, imageUrl){
        const postIndex = posts.findIndex((p)=>p.id == id && p.userId == userId);
        if(postIndex != -1){
            posts[postIndex].caption = caption;
            posts[postIndex].imageUrl = imageUrl;
            return {success:true, msg:posts[postIndex]};
        } else {
            return {success: false, msg: 'Please Enter valid ID !!!'};
        }
    }

    static delete(id, userId){
        const postIndex = posts.findIndex((p)=>p.id == id && p.userId == userId);
        if(postIndex == -1){
            return {success:false, msg: "operation not allowed"};
        } else {
            const deletedItem = posts.splice(postIndex, 1);
            return {success: true, msg:'1 Item deleted'}
        }
    }

    static checkPostId(postId){
        // const postIdList = posts.forEach((p)=> p.id == postId);
        // console.log(postIdList);
        const validcheck = posts.find((p)=>p.id == postId);
        console.log(validcheck);
        return validcheck;
    }

    static filter(caption){
        const data = posts.filter((p)=>{
            return p.caption == caption;
        })
        return data;
    }
    static addDraft(post){
        post.id = posts.length + 1;
        drafts.push(post)
        return {success: true, msg:'Post Draft Added Sccessfully !!!'};
    }
}

var posts = [
    new PostModel(
        1,
        1,
        'Travel',
        'https://m.media-amazon.com/images/I/51-nXsSRfZL._SX328_BO1,204,203,200_.jpg',
    )
]

var drafts = [];