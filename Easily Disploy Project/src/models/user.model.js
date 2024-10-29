
export default class UserModel {
    constructor(id, username, email, password){
        this.id=id;
        this.username = username;
        this.email = email;
        this.password = password;
    } 

    static add(username, email, password){
        const newUser = new UserModel(users.length+1, username, email, password)

        users.push(newUser);
    }
    static check(email, password){
        // users.map((user)=>user.email == email && user.password == password);
        const result = users.find((u) => u.email == email && u.password == password);
        return result;
        // return true;
    }

}

var users = [
    {
        id:1,
        name: 'Mayur Myatra',
        email: 'max@gmail.com',
        password: '12345',
    }
];