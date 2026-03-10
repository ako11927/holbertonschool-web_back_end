export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }
}

export class StudentHolberton extends HolbertonCourse {}
