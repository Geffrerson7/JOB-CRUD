function deleteJobConfirmation(event,jobId) {
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
      Swal.fire("Deleted!", "Your job has been deleted.", "success");
      window.location.href = `/delete-job/${jobId}`;
    }
  });
}
