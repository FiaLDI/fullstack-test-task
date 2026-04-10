"use client";

import { AddFileFormModal } from "@/features/add-file";
import { UiPack } from "@/shared";
import { ListAlerts, ListFiles, ManagementFiles } from "@/widgets";
import { usePage } from "./usePage";

export default function Page() {

  const { Alert, Col, Container, Row } = UiPack;

  const {
    files,
    alerts,
    showModal,
    setShowModal,
    errorMessage,
    isLoading,
    handleLoad,
    handleSubmit
  } = usePage();

  return (
    <Container fluid className="py-4 px-4 bg-light min-vh-100">
      <Row className="justify-content-center">
        <Col xxl={10} xl={11}>
          <ManagementFiles loadData={handleLoad} setShowModal={setShowModal} />

          {errorMessage && (
            <Alert variant="danger" className="shadow-sm">
              {errorMessage}
            </Alert>
          )}

          <ListFiles files={files} isLoading={isLoading}/> 
          <ListAlerts alerts={alerts} isLoading={isLoading} />
        </Col>
      </Row>

      <AddFileFormModal 
        handleSubmit={handleSubmit} 
        showModal={showModal} 
        setShowModal={setShowModal}
      />
    </Container>
  );
}
