export class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }
}

export class StudentHolberton {
  constructor(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;
  }

  fullStudentDescription() {
    return `${this._firstName} ${this._lastName}`;
  }
}

export const listOfStudents = [
  new StudentHolberton('Guillaume', 'Salva'),
  new StudentHolberton('John', 'Doe'),
  new StudentHolberton('Albert', 'Clinton'),
  new StudentHolberton('Donald', 'Bush'),
  new StudentHolberton('Jason', 'Sandler'),
];
