
export default class UserModel{
    constructor(id, name, email, password){
        this.id = id;
        this.name = name;
        this.email = email;
        this.password = password;
    }

    static signup(name, email, password){
        let id = users.length + 1
        const newUser = new UserModel(
            id,
            name,
            email,
            password
        )
        // console.log(newUser)
        users.push(newUser);
        return {status: true, msg: newUser};
    }

    static login(email, password){
        const user = users.find((u)=>u.email == email && u.password == password);
        // console.log(user);
        if(!user){
            return {status:false, msg:"Invalid Credentials"};
        }
        return {status:true, msg: user}
    }

    static getAll(){
        return users;
    }

}

let users = [
    {
        id: 1,
        name: 'Mayur',
        email: 'max@gmail.com',
        password: '12345'
    }
]