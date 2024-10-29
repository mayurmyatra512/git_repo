// Please don't change the pre-written code
// Import the necessary modules here

export default class ArtPiece {
  constructor(id, title, artist, year, imageUrl) {
    this.id = id;
    this.title = title;
    this.artist = artist;
    this.year = year;
    this.imageUrl = imageUrl;
  }

  static db = [];

  static create({ title, artist, year, imageUrl }) {
    const artPiece = new ArtPiece(
      ArtPiece.db.length + 1,
      title,
      artist,
      year,
      imageUrl
    );
    ArtPiece.db.push(artPiece);
    return artPiece;
  }

  static findAll(query) {
    // Write your code here to retrieve all art pieces
    return ArtPiece.db;
  }

  static findOne(id) {
    const art = ArtPiece.db.find((data)=> data.id == id);
    return art;
    // Write your code here to retrieve a specific art piece by its id
  }

  static update(id, data) {
    const { title, artist, year, imageUrl } = data;
    const index = ArtPiece.db.findIndex((data)=> data.id == id);

    ArtPiece.db[index].title = title;
    ArtPiece.db[index].artist = artist;
    ArtPiece.db[index].year = year;
    ArtPiece.db[index].imageUrl = imageUrl;

    return ArtPiece.db[index];
    // Write your code here to update the details of a specific art piece
  }

  static delete(id) {
    const index = ArtPiece.db.findIndex((data)=> data.id == id);
    ArtPiece.db.splice(index, 1);
    // Write your code here to delete a specific art piece
  }
}
