function createJob(event) {
    event.preventDefault(); 

    const form = event.target;
    const formData = new FormData(form);

    fetch("/new-job", {
      method: "POST",
      body: formData,
    }).then((response) => {
      if (response.ok) {
        Swal.fire({
          title: "Success",
          text: "Job created successfully",
          icon: "success",
        }).then((result) => {
          if (result.isConfirmed) {
            window.location.href = "/";
          }
        });
      } else {
        Swal.fire({
          title: "Error",
          text: "Failed to create job",
          icon: "error",
        });
      }
    });
  }