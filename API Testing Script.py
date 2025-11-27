import requests
BASE_URL = "https://reqres.in/api"
params = {"apiKey": "     "}
def test_get_users():
    response = requests.get(f"{BASE_URL}/users?page=2")
    # assert <condition>, <optional_error_message>
    assert response.status_code == 200 , f"API FAILED ******* Status code: {response.status_code}"
    # print("Status Code:", response.status_code)
    body=response.json()
    assert "data" in body   , "no 'data' keyword found"
    print("Response JSON:", body)
    assert len(body["data"]) >0 , "User list is empty"

def test_create_user():
    payload = {
    "id": 13,
    "email": "QA@qa",
    "first_name": "Ales",
    "last_name": "Ales"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload,params=params)
    data= response.json()
    print (response.json())
    # data posted
    assert response.status_code == 201 , f"API FAILED ******* Status code: {response.status_code}"

def test_Update_user():
    user_id = 7
    update_payload = {
        "email": "QA@qa",
        "first_name": "Ales",
        "last_name": "Ales"
    }
    response = requests.patch(f"{BASE_URL}/users/{user_id}", json=update_payload ,params=params)
    data= response.json()

    assert response.status_code == 200 , f"API FAILED ******* Status code: {response.status_code}"

    for key, value in update_payload.items():
        assert response_body.get(key) == value, f"Mismatch for {key}: expected {value}, got {response_body.get(key)}"


some chunck of API calls from univerty final year project:
------------------------------------*****************---------------------------------------------


API CALL    Method : POST

const AddProgramme = async (Title, Description, Category, Date, NgoDetails) => {
    const res = await fetch('http://localhost:3001/AddProgramme', {
    method: 'POST',
    body: JSON.stringify({
        Title: Title,
        Description: Description,
        Category: Category,
        Date: Date,
        NGO: NgoDetails.Name
    }),
    headers: {
        'Content-Type': 'application/json',
    },
});

const result = await res.json();

if (result.status === 'SUCCESS') {
    toast.success('Programme Added Successfully');
} else if (result.status === 'FAILURE') {
toast.error("Error While Adding Programme");
}
};
-----------------------------------*****************************------------------------------------
API CALL   Method : delete 
const DeletePost = async (ID) => {
    const res = await fetch('http://localhost:3001/DeleteRestaurantPost', {
    method: 'DELETE',
    body: JSON.stringify({ id: ID }),
    headers: {
        'Content-Type': 'application/json',
    },
});

const result = await res.json();

if (result.status === 'SUCCESS') {
    toast.success('Post Deleted Successfully');
} else if (result.status === 'FAILURE') {
toast.error("Error while deleting post. Kindly reload.");
}
};
