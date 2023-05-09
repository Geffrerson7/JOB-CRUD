function deleteJobConfirmation(event, jobId) {
  event.preventDefault();
  Swal.fire({
    title: "Are you sure?",
    text: "You will not be able to recover this job!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Yes, delete it!",
  }).then((result) => {
    if (result.isConfirmed) {
      fetch(`/delete-job/${jobId}`, {
        method: "DELETE",
      })
        .then((response) => {
          if (response.ok) {
            Swal.fire({
              title: "Deleted!",
              text: "Your job has been deleted.",
              icon: "success",
            }).then(() => {
              location.reload();
            });
          } else {
            Swal.fire({
              title: "Error",
              text: "Failed to delete job",
              icon: "error",
            });
          }
        })
        .catch((error) => console.error("Error:", error));
    }
  });
}