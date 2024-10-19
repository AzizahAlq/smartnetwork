<CycloneDDS>
  <Domain id="0">
    <Participants>
      <Participant name="Router1">
        <Topics>
          <Topic name="RouterMetrics" type="std_msgs::String"/>
        </Topics>
        <Publishers>
          <Publisher>
            <DataWriter topic="RouterMetrics"/>
          </Publisher>
        </Publishers>
      </Participant>
    </Participants>
  </Domain>
</CycloneDDS>
