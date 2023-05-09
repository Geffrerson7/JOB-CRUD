function updateJob(event, jobId) {
  event.preventDefault();

  const form = event.target;
  const formData = new FormData(form);

  fetch(`/update-job/${jobId}`, {
    method: "PUT",
    body: formData,
  }).then((response) => {
    if (response.ok) {
      Swal.fire({
        title: "Success",
        text: "Job updated successfully",
        icon: "success",
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.href = "/";
        }
      });
    } else {
      Swal.fire({
        title: "Error",
        text: "Failed to update job",
        icon: "error",
      });
    }
  });
}
