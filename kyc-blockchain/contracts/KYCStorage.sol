pragma solidity ^0.8.0;

contract KYC {
    struct User {
        string name;
        string birthDate;
    }

    mapping(address => User) public users;

    function storeKYC(string memory _name, string memory _birthDate) public {
        users[msg.sender] = User(_name, _birthDate);
    }

    function getKYC(address _user) public view returns (string memory, string memory) {
        User memory user = users[_user];
        return (user.name, user.birthDate);
    }
}
