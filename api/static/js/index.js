let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2] },
        { orderable: false, targets: [] },
        { searchable: false, targets: [] }
    ],
    pageLength: 3,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listCursos();

    dataTable = $("#datatable-cursos").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listCursos = async () => {
    try {
        const response = await fetch("dpg-chdrjlu7avj22bgoph90-a.oregon-postgres.render.com:5432/app/list_cursos/");
        const data = await response.json();

        let content = ``;
        data.cursos.forEach((curso, index) => {
            content += `
                    <tr>
                    <td class="centered">${index + 1}</td>
                    <td class="centered">
                    <div class="card text-dark bg-light mb-3" style=" width:21rem; height:7rem;">
  <div class="row g-0">
  <div class="col-md-4">
      <img src="${curso.img_url}" class="img-fluid rounded-start" alt="...">
    </div>
    <div class="col-md-8">
      <div class="card-body">
      <h6 class="card-title">${curso.name}</h6>
      
      <div>
      <a type="button" href="${curso.curso_url}" class="btn btn-outline-primary" style=" width:7.5rem; height:2.2rem;" target="_blank">Ver Producto</a>
      </div>
      </div>
      </div>
      </div>
      </div>    
                   </td>
                   <td class="centered"><p class="card-text" style=" width:24rem; height:8rem;">${curso.description}</p></td>
                    <td class="centered">${curso.category}</td>
                    </tr>`;
        });
        tableBody_cursos.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});
