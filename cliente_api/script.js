async function login() {

    const response = await fetch(
        "http://127.0.0.1:8000/o/token/",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                grant_type: "password",
                username: document.getElementById("username").value,
                password: document.getElementById("password").value,
                client_id: "MUfurTaBQ1Fat4v7ivZfK2yOulwZWjFvF449ZILm",
                client_secret: "ToWllv1Yhqa1ddG8b9yD8o1HUwBMuytwwv8mluzx8od8Zc1f9FX9i74gq4kiqM8I4wKW6uJMlyaYj4qLcXDytNLVvLiu4NSPfqQE5ZKaerdXM0VFYOHeCL1T18l3KLxR"
            })
        }
    );

    const data = await response.json();

    if (data.access_token) {

        localStorage.setItem(
            "token",
            data.access_token
        );

        alert("Login realizado com sucesso!");

    } else {

        alert("Erro ao realizar login");
        console.log(data);

    }
}

async function listarCursos() {

    const token =
        localStorage.getItem("token");

    const response = await fetch(
        "http://127.0.0.1:8000/api/cursos/",
        {
            headers: {
                "Authorization":
                    "Bearer " + token
            }
        }
    );

    const cursos =
        await response.json();

    const lista =
        document.getElementById("listaCursos");

    lista.innerHTML = "";

    cursos.forEach(curso => {

        const item =
            document.createElement("li");

        item.innerHTML = `
            <strong>${curso.nome}</strong>
            <br>
            ${curso.descricao}
        `;

        lista.appendChild(item);

    });
}